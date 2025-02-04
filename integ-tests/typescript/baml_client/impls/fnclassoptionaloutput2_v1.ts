// This file is auto-generated. Do not edit this file manually.
//
// Disable formatting for this file to avoid linting errors.
// tslint:disable
// @ts-nocheck
/* eslint-disable */


import { GPT35 } from '../client';
import { FnClassOptionalOutput2 } from '../function';
import { schema } from '../json_schema';
import { Deserializer } from '@boundaryml/baml-core/deserializer/deserializer';


const prompt_template = `\
Return a json blob for the following input:
{//BAML_CLIENT_REPLACE_ME_MAGIC_input//}

Answer in JSON using this schema:
{
  "prop1": string | null,
  "prop2": string | null,
  "prop3": {
    "prop4": string | null
  } | null
} | null

JSON:\
`;

const deserializer = new Deserializer<ClassOptionalOutput2 | null>(schema, {
  $ref: '#/definitions/FnClassOptionalOutput2_output'
});

FnClassOptionalOutput2.registerImpl('v1', async (
  arg: string
): Promise<ClassOptionalOutput2 | null> => {
  
    const result = await GPT35.run_prompt_template(
      prompt_template,
      [
        "{//BAML_CLIENT_REPLACE_ME_MAGIC_input//}",
      ],
      {
        "{//BAML_CLIENT_REPLACE_ME_MAGIC_input//}": arg,
      }
    );

    return deserializer.coerce(result.generated);
  }
);


