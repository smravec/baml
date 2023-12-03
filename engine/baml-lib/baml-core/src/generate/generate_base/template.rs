use handlebars::handlebars_helper;

use super::{file::File, traits::TargetLanguage};

#[derive(Debug)]
pub(super) enum HSTemplate {
    Function,
    FunctionPYI,
    Enum,
    Class,
    Client,
    BAMLClient,
    Variant,
    RetryPolicy,
    SingleArgTestSnippet,
    MultiArgTestSnippet,
}

handlebars_helper!(BLOCK_OPEN: |*_args| "{");
handlebars_helper!(BLOCK_CLOSE: |*_args| "}");
fn init_hs() -> handlebars::Handlebars<'static> {
    let mut reg = handlebars::Handlebars::new();
    reg.register_helper("BLOCK_OPEN", Box::new(BLOCK_OPEN));
    reg.register_helper("BLOCK_CLOSE", Box::new(BLOCK_CLOSE));

    reg
}

macro_rules! include_template {
    ($lang:expr, $type:expr, $file:expr) => {
        include_str!(concat!(
            "../generate_",
            $lang,
            "_client",
            "/",
            "templates/",
            $type,
            "/",
            $file,
            ".hbs"
        ))
    };
}

macro_rules! register_partial_file {
    ($reg:expr, $lang:expr, $type:expr, $file:expr) => {
        register_partial!(
            $reg,
            $file,
            match $lang {
                TargetLanguage::Python => include_template!("python", $type, $file),
                TargetLanguage::TypeScript => include_template!("ts", $type, $file),
            }
        );
    };
}

macro_rules! register_partial {
    ($reg:expr, $name:expr, $template:expr) => {
        $reg.register_partial($name, $template)
            .unwrap_or_else(|e| panic!("Failed to register template: {}", e));
    };
}

fn use_partial_py(
    lang: TargetLanguage,
    template: HSTemplate,
    reg: &mut handlebars::Handlebars<'static>,
    f: &mut File,
) -> String {
    register_partial!(reg, "print_code", "{{{code}}}");
    match template {
        HSTemplate::Variant => {
            register_partial_file!(reg, lang, "functions", "arg_list");
            register_partial_file!(reg, lang, "functions", "arg_values");
            register_partial_file!(reg, lang, "functions", "func_def");
            f.add_import("baml_lib._impl.deserializer", "Deserializer");

            register_partial_file!(reg, lang, "functions", "variant");
            String::from("variant")
        }
        HSTemplate::BAMLClient => {
            register_partial_file!(reg, lang, "export", "generated_baml_client");
            f.add_import("baml_core.services", "LogSchema");
            f.add_import("baml_core.otel", "add_message_transformer_hook");
            f.add_import("baml_core.otel", "flush_trace_logs");
            f.add_import("baml_lib", "baml_init");
            f.add_import("typing", "Optional");
            f.add_import("typing", "Callable");
            f.add_import("typing", "List");
            f.add_import("baml_core.services.api_types", "LogSchema");

            String::from("generated_baml_client")
        }
        HSTemplate::Client => {
            register_partial_file!(reg, lang, "types", "client");
            f.add_import("baml_core.provider_manager", "LLMManager");
            String::from("client")
        }
        HSTemplate::RetryPolicy => {
            register_partial_file!(reg, lang, "configs", "retry_policy");
            String::from("retry_policy")
        }
        HSTemplate::Class => {
            register_partial_file!(reg, lang, "types", "class");
            f.add_import("pydantic", "BaseModel");
            f.add_import("baml_lib._impl.deserializer", "register_deserializer");
            String::from("class")
        }
        HSTemplate::Enum => {
            register_partial!(reg, "enum_value", r#"{{name}} = "{{name}}""#);
            register_partial_file!(reg, lang, "types", "enum");
            f.add_import("enum", "Enum");
            f.add_import("baml_lib._impl.deserializer", "register_deserializer");
            String::from("enum")
        }
        HSTemplate::Function => {
            register_partial_file!(reg, lang, "functions", "arg_list");
            register_partial_file!(reg, lang, "functions", "method_def");

            register_partial_file!(reg, lang, "functions", "interface");
            f.add_import("typing", "runtime_checkable");
            f.add_import("typing", "Protocol");

            register_partial_file!(reg, lang, "functions", "function_py");
            f.add_import("baml_lib._impl.functions", "BaseBAMLFunction");
            String::from("function_py")
        }
        HSTemplate::FunctionPYI => {
            register_partial_file!(reg, lang, "functions", "arg_list");
            register_partial_file!(reg, lang, "functions", "method_def");

            register_partial_file!(reg, lang, "functions", "interface");
            f.add_import("typing", "runtime_checkable");
            f.add_import("typing", "Protocol");

            register_partial_file!(reg, lang, "functions", "function_pyi");
            String::from("function_pyi")
        }
        HSTemplate::SingleArgTestSnippet => {
            register_partial_file!(reg, lang, "tests", "single_arg_snippet");
            f.add_import(".__do_not_import.generated_baml_client", "baml");
            f.add_import("baml_lib._impl.deserializer", "Deserializer");
            String::from("single_arg_snippet")
        }
        HSTemplate::MultiArgTestSnippet => {
            register_partial_file!(reg, lang, "tests", "multi_arg_snippet");
            f.add_import("json5", "loads # type: ignore");
            f.add_import(".__do_not_import.generated_baml_client", "baml");
            f.add_import("baml_lib._impl.deserializer", "Deserializer");
            String::from("multi_arg_snippet")
        }
    }
}

pub(super) fn render_template(
    language: TargetLanguage,
    template: HSTemplate,
    f: &mut File,
    json: serde_json::Value,
) {
    let mut reg = init_hs();
    let template = use_partial_py(language, template, &mut reg, f);
    match reg.render_template(&format!("{{{{> {}}}}}", template), &json) {
        Ok(s) => f.add_string(&s),
        Err(e) => panic!("Failed to render template: {}", e),
    }
}
