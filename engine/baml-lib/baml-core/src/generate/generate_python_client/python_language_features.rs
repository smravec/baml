use std::collections::{HashMap, HashSet};

use crate::generate::dir_writer::{FileCollector, Import, LanguageFeatures, LibImport};

pub(super) struct PythonLanguageFeatures {}

impl LanguageFeatures for PythonLanguageFeatures {
    fn content_prefix(&self) -> &'static str {
        r#"
# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
        "#
        .trim()
    }

    fn format_exports(&self, exports: &Vec<String>) -> String {
        if !exports.is_empty() {
            let mut buffer = String::new();
            let mut exports = exports.clone();
            exports.sort();
            buffer.push_str("\n\n__all__ = [\n");
            buffer.push_str(
                &exports
                    .iter()
                    .fold(String::new(), |mut buffer, name| {
                        buffer.push_str(&format!("    '{}',\n", name));
                        buffer
                    })
                    .trim_end_matches(",\n"),
            );
            buffer.push_str("\n]\n");
            buffer
        } else {
            String::new()
        }
    }

    fn format_imports(&self, libs: &HashSet<LibImport>, imports: &Vec<Import>) -> String {
        // group imports by lib
        let mut imports_by_lib = imports
            .iter()
            .fold(HashMap::new(), |mut map, import| {
                let imports = map.entry(&import.lib).or_insert(HashSet::new());
                imports.insert(import);
                map
            })
            .into_iter()
            .collect::<Vec<_>>();
        imports_by_lib.sort_by(|a, b| a.0.cmp(b.0));

        imports_by_lib
            .iter()
            .fold(String::new(), |mut buffer, (lib, imports)| {
                buffer.push_str(&format!("from '{}' import ", lib));
                buffer.push_str(
                    &imports
                        .iter()
                        .fold(String::new(), |mut buffer, import| {
                            match import.as_name {
                                Some(ref as_name) => {
                                    buffer.push_str(&format!("{} as {}", import.name, as_name));
                                }
                                None => {
                                    buffer.push_str(&import.name);
                                }
                            }
                            buffer.push_str(", ");
                            buffer
                        })
                        .trim_end_matches(", "),
                );
                buffer.push_str("\n");
                buffer
            })
    }

    fn to_file_path(&self, path: &str, name: &str) -> std::path::PathBuf {
        std::path::PathBuf::from(format!("{}/{}.py", path, name).to_lowercase())
    }
}

pub(super) trait ToPython {
    fn to_py(&self) -> String;
}

pub(super) type PythonFileCollector = FileCollector<PythonLanguageFeatures>;

pub(super) fn get_file_collector() -> PythonFileCollector {
    PythonFileCollector::new(PythonLanguageFeatures {})
}
