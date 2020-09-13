# Unilab Demo API
რეპოზიტორია წარმოადგენს NLTK ბიბლიოთეკის გარშემო აწყობილ საცდელ API-ს


## Documentation

ვებ სერვისის გამოყენება შეგიძლიათ შესაბამის მისამართზე მოთხოვნის გასაგზავნად.

მოთხოვნის მისამართი და მოთხოვნის body შეგიძლიათ ნახოთ მეთოდების ჩამონათვალში

## Instruction

> 1. დაამატეთ /resource დირექტორიაში ახალი ვებ API რესურსი რომელსაც ძირითად აპლიკაციაში შემოიყვანთ შესაბამის endpoint-ზე მისაწვდომად.
> 2. დაამატეთ README.md ფაილის მეთოდების ქვეშ თქვენს რესურსზე სამუშაოდ გამიზნული მოთხოვნის მაგალითი.

## Methods:

### Postman-ის კოლექციასთან სამუშაოდ:  [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/04c67bb43adc0e74b22f)

[<img align="middle" width="150" src="https://edit.blog.postman.com/wp-content/uploads/2015/08/postman-logo-drawing-board.png">](https://app.getpostman.com/join-team?invite_code=78f92fcf5753f9fcc222ed95db9052ca) 

პოსტმენის ლოგოზე დაწოლით შენ შეძლებ შემოუერთდე ჩვენს პოსტმენის სამუშაო გუნდს, სადაც ერთად შევძლებთ API-ს საერთო კოლექციის და მის დოკუმენტაციის აწყობას.

**TemSentenceTokenizer**
>
> სერვისი მოთხოვნილ წინადადებას უკეთებს ტოკენიზაციას და აბრუნებს ტოკენიზებულ სიას
> ``` 
> endpoint: _/TemSenTok_
> type: GET 
> body: {
> "sentence" : "This is my demo sentence"
> } 
> ```
> 
**FrequencyDistribution**
>
> სერვისი მოთხოვნილ ტექსტს უკეთებს ტოკენიზაციას და აბრუნებს სიტყვების სიხშირის განაწილების სიას
> ``` 
> endpoint: _/FreqDist_
> type: GET 
> body: {
> "text" : "This is my demo text"
> } 
> ```

**GroupingMultiplePatters**
>
> სერვისი მოთხოვნილ ტექსტს უკეთებს ტოკენიზაციას და აბრუნებს სიმბოლოებისგან გაწმენდილ ტექსტს
> ``` 
> endpoint: _/GMultiplePatterns_
> type: GET 
> body: {
> "text" : "This is my demo sentence"
> } 
> ```

**Chunk_CleanSentences**
>
> Devides and clears the sentence of punctuation marks and builds a dependency tree on each sentence. Allocates its own names and verbs.
> ``` 
> endpoint: _/Chunk
> type: GET 
> body: {
> "text" : "Any Text"

**DepTreeSvgMaker**
>
> Created dependency tree svg image and returns
> ``` 
> endpoint: _/DepTree
> type: GET 
> body: {
> "sentence" : "Any Text"
