{{#if unnamed_args}}
{{> arg_list}}
{{else}}
*, {{> arg_list}}
{{/if}}