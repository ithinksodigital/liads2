
//Limit characters inside job description text field
var content_id = 'jobDescription';
max = 200;
//binding keyup/down events on the contenteditable div
$('#'+content_id).keyup(function(e){ check_charcount(content_id, max, e); });
$('#'+content_id).keydown(function(e){ check_charcount(content_id, max, e); });

function check_charcount(content_id, max, e)
{
    if(e.which != 8 && $('#'+content_id).text().length > max)
    {
       // $('#'+content_id).text($('#'+content_id).text().substring(0, max));
       e.preventDefault();
    }
}


// limit characters on apply

var content_id1 = 'jobEmail';
max1 = 45;
//binding keyup/down events on the contenteditable div
$('#'+content_id1).keyup(function(e){ check_charcount(content_id1, max1, e); });
$('#'+content_id1).keydown(function(e){ check_charcount(content_id1, max1, e); });

function check_charcount(content_id1, max1, e)
{
    if(e.which != 8 && $('#'+content_id1).text().length > max1)
    {
       // $('#'+content_id).text($('#'+content_id).text().substring(0, max));
       e.preventDefault();
    }
}


// creating utm link & capture picture

function catch_img() {
    let jobId = document.getElementById("jobId").value;
    if (jobId !== '') {
        window.scrollTo(0,0);

    url = `<p>https://m.hays.pl/Job/Detail/PL_${jobId}?utm_source=linkedin&utm_medium=social&utm_campaign=consultant_graphics&utm_content=${jobId}&jobSource=ConsultantGraphics</p>`
        document.getElementById("job-ga-link-expl").innerHTML = 'Skopiuj swój unikalny link i wklej go wraz z grafiką na Linkedin. ';
        document.getElementById("job-ga-link").innerHTML = url;
               html2canvas($('#capture')[0], {
                      scale:1
                    }).then(function(canvas) {
                      var a = document.createElement('a');
                      a.href = canvas.toDataURL("image/png");
                      // {#let title = document.getElementById(jobId).textContent;#}
                      let file_name = document.getElementById("jobId").value;
                      a.download =  `linkedin_${file_name}.png`;
                      a.click();
                    });
    }
    else {
        document.getElementById("job-ga-link-expl").innerHTML = 'Wpisz numer referencyjny ogłoszenia.';

        alert("Wpisz numer referencyjny ogloszenia.")
    }
}

// prevent paste with formating


document.querySelector("div[contenteditable]").addEventListener("paste", function(e) {
e.preventDefault();
var text = e.clipboardData.getData("text/plain");
document.execCommand("insertHTML", false, text);
});
document.getElementById('jobLocation').addEventListener("paste", function(e) {
e.preventDefault();
var text = e.clipboardData.getData("text/plain");
document.execCommand("insertHTML", false, text);
});
document.getElementById('jobDescription').addEventListener("paste", function(e) {
e.preventDefault();
var text = e.clipboardData.getData("text/plain");
document.execCommand("insertHTML", false, text);
});
document.getElementById('jobEmail').addEventListener("paste", function(e) {
e.preventDefault();
var text = e.clipboardData.getData("text/plain");
document.execCommand("insertHTML", false, text);
});


//adding logo on "picture"
/*
var elem = document.createElement("img");
elem.setAttribute("src", "{{ specialism.specialism_logo.specialism_file.url }}");
elem.setAttribute("height", "26");
elem.setAttribute("width", "231");
elem.setAttribute("alt", "hays logo");
elem.setAttribute("style",  "padding-left:70px; top: 460px;")
document.getElementById("capture").appendChild(elem);
*/

