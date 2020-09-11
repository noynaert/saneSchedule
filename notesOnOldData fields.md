
BaseURL:  https://aps4.missouriwestern.edu/schedule/?tck=202120

Failed curl test: curl -F "course_number=''" -F "subject=ALL" -F "department=HON" -F "display_closed=yes" -F "course-type=all" https://aps4.missouriwestern.edu/schedule/Default.asp?tck=202120 > test.html

Post Fields for a search by department:
course_number=""
subject="ALL"
department=  [[departmentID]]
display_closed="yes"
course_type="all"

BIO Biology
BUS Business
CHE Chemistry
COM Communication
...

From the web page (fall, 2020)

```html
<option value="AF">Academic Affairs</option>
					
					<option value="BIO">Biology</option>
					
					<option value="BUS">Business</option>
					
					<option value="CHE">Chemistry</option>
					
					<option value="COM">Communication</option>
					
					<option value="CSMP">Comp Science, Math & Physics</option>
					
					<option value="CJLG">Crim Justice & Legal Studies</option>
					
					<option value="EDU">Education</option>
					
					<option value="ET">Engineering Technology</option>
					
					<option value="FIN">Fine Arts</option>
					
					<option value="HP">Health Professions</option>
					
					<option value="HON">Honors Program</option>
					
					<option value="MIL">Military Science</option>
					
					<option value="NURS">Nursing</option>
					
					<option value="PSY">Psychology</option>
					
					<option value="SSH">Social Sciences & Humanities</option>
```

```groovy
From an old project:


import org.jsoup.Connection
import org.jsoup.Jsoup
import org.jsoup.nodes.Document
import org.jsoup.select.Elements

class Reprise {
    static def getSections(String dept){
        Section sec = null;
        def baseURL = "https://aps2.missouriwestern.edu/schedule/Default.asp?tck=201910"


        Document doc = null;

        Connection.Response response = Jsoup.connect(baseURL)
        .timeout(60 * 1000)
        .method(Connection.Method.POST)
        .data("course_number","")
        .data("subject","ALL")
        .data("department", dept)
        .data("display_closed", "yes")
        .data("course_type","ALL")
        .followRedirects(true)
        .execute();

        doc = response.parse()

        //doc = Jsoup.parse(new File(department+".html"),"UTF-8")

        //System.out.println(doc)
        Elements rows = doc.select("tr")
        println("There are ${rows.size()} rows")

        rows.each{ row->
            def className = row.attr("class")
            println "Row: $row "
            Elements cells = row.select("td")
            if(className == "list_row"){
                if(sec != null){
                    println sec   //Add to database here!
                    sec = new Section()
                }
                //Going to be some code here
              //  sec.department = dept
              //  sec.crn = cells.get(0).text().trim();  //works in Java or groovy
              //  sec.courseID = cells[1].text().trim()  //only works in groovy
            }

        }

    }
}
```
