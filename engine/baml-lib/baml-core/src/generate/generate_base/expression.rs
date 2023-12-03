use internal_baml_schema_ast::ast::Expression;

use super::{
    file::{escaped_string, File},
    traits::WithToObject,
    TargetLanguage,
};

impl WithToObject for Expression {
    fn to_ts_object(&self, f: &mut File) -> String {
        let language = TargetLanguage::TypeScript;
        match self {
            Expression::NumericValue(val, _) => val.clone(),
            Expression::StringValue(val, _) => {
                format!("\"{}\"", escaped_string(val, ("\"", "\\\"")))
            }
            Expression::RawStringValue(val) => {
                format!("`{}`", escaped_string(val.value(), ("`", "\\`")))
            }
            Expression::Identifier(idn) => idn.to_object(f, language),
            Expression::Array(arr, _) => {
                let json_arr: Vec<_> = arr.iter().map(|x| x.to_object(f, language)).collect();
                format!("[{}]", json_arr.join(", "))
            }
            Expression::Map(map, _) => {
                let kvs = map
                    .iter()
                    .map(|(k, v)| {
                        let key = k.to_object(f, language);
                        let value = v.to_object(f, language);
                        (key, value)
                    })
                    .map(|(k, v)| format!("{}: {}", k, v))
                    .collect::<Vec<_>>()
                    .join(", ");
                format!("{{{}}}", kvs)
            }
        }
    }

    fn to_py_object(&self, f: &mut File) -> String {
        let language = TargetLanguage::Python;
        match self {
            Expression::NumericValue(val, _) => val.clone(),
            Expression::StringValue(val, _) => {
                format!("\"{}\"", escaped_string(val, ("\"", "\\\"")))
            }
            Expression::RawStringValue(val) => format!(
                "\"\"\"\\\n{}\\\n\"\"\"",
                escaped_string(val.value(), ("\"\"\"", "\\\"\\\"\\\""))
            ),
            Expression::Identifier(idn) => idn.to_object(f, language),
            Expression::Array(arr, _) => {
                let json_arr: Vec<_> = arr.iter().map(|x| x.to_object(f, language)).collect();
                format!("[{}]", json_arr.join(", "))
            }
            Expression::Map(map, _) => {
                let kvs = map
                    .iter()
                    .map(|(k, v)| {
                        let key = k.to_object(f, language);
                        let value = v.to_object(f, language);
                        (key, value)
                    })
                    .map(|(k, v)| format!("{}: {}", k, v))
                    .collect::<Vec<_>>()
                    .join(", ");
                format!("{{{}}}", kvs)
            }
        }
    }
}
