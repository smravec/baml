enum TestEnum {
  A @alias("k1") @description(#"
    User is angry
  "#)
  B @alias("k22") @description(#"
    User is happy
  "#)
  // tests whether k1 doesnt incorrectly get matched with k11
  C @alias("k11") @description(#"
    User is sad
  "#)
  D @alias("k44") @description(
    User is confused
  )
  E @description(
    User is excited
  )
  F @alias("k5") // only alias
  
  G @alias("k6") @description(#"
    User is bored
    With a long description
  "#)

  @@alias("Category")
}
 
function FnTestAliasedEnumOutput {
  input string
  output TestEnum
}

impl<llm, FnTestAliasedEnumOutput> v1 {
  client GPT35

  override TestEnum {
    B @description(#"
      Another super long
      description
      with multiple lines
    "#)
  }

  prompt #"
    Classify the user input into the following category
     
    {#print_enum(TestEnum)}
    ---

    input: {#input}

    Category ID:
  "#
}