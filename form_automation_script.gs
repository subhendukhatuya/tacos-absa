 function createForm() {
   // create & name Form
   var item = "Annotate Aspect of Sentences";
   var form = FormApp.create(item)
    //   .setTitle(item);

   // single line text field
   item = "Reviewer Name";
   form.addTextItem()
       .setTitle(item)
       .setRequired(true);
 // Change URL accordingly
var sentence_sheet = SpreadsheetApp.openByUrl("https://docs.google.com/spreadsheets/d/10ZqjhRbwwffG6R0xpp96lLjNj4B34fhKh7V1nhRAL80/edit#gid=557102824").getDataRange().getValues();

for (var sentence_index = 0; sentence_index < sentence_sheet.length-1; sentence_index++) {
  sentence = sentence_sheet[sentence_index+1][0];

  form.addTextItem()
      .setTitle(sentence)
      .setRequired(true);

}
