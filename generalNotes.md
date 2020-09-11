# General Notes for the Backend team

## Things we have figured out so far

## Friday, 2020-09-04, 1100

- The Udemy course is a lot cheaper in dollars than in euros!
- Mesmin has learned jsoup for python and is having success scraping pages
- Nick is going to work on firefox
- Meeting, hopefully on Monday

## Friday, 2020-09-11, 1100

- Web scraping:  Here is a curl that works:

```text
curl -d "course_numbr=&subject=ALL&department=HON&display_closed=yes&course-type=all" -X POST  https://aps4.missouriwestern.edu/schedule/Default.asp?tck=202120 > test.html
```

-Nick is going to set up a sample database in Firebase
-Frontend encouraged to set up a sample project that can try to pull from Nick's sample database.  The Udemy course uses firebase, so there should be a good example.
