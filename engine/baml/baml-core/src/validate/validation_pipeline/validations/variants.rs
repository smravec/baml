use internal_baml_diagnostics::{DatamodelError, Span};

use crate::{ast::WithSpan, validate::validation_pipeline::context::Context};

pub(super) fn validate(ctx: &mut Context<'_>) {
    for variant in ctx.db.walk_variants() {
        if variant.walk_function().is_none() {
            ctx.push_error(DatamodelError::new_validation_error(
                &format!("Function not found: {}", variant.function_name()),
                variant.ast_variant().span().clone(),
            ));
        }

        let client = &variant.properties().client;

        if ctx.db.find_client(client).is_none() {
            ctx.push_error(DatamodelError::new_validation_error(
                &format!("Unknown client `{}`", client.as_str()),
                variant.ast_variant().span().clone(),
            ));
        }
        validate_prompt(
            ctx,
            &variant.properties().prompt,
            &variant.ast_variant().span(),
        );
    }
}

fn validate_prompt(ctx: &mut Context<'_>, prompt: &str, span: &Span) {
    if prompt.is_empty() {
        ctx.push_error(DatamodelError::new_validation_error(
            "Prompt cannot be empty",
            span.clone(),
        ));
    }
}