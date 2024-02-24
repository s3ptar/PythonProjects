 /***********************************************************************
*! \fn          function leadingzero (number)
*  \brief       set leading zero to numer
*  \param       number
*  \exception   none
*  \return      number with leading
 ***********************************************************************/             
function leadingzero (number) {
    return (number < 10) ? '0' + number : number;
}

/***********************************************************************
*! \fn          int16_t create_fb(char *dataPtr, byte *fb)
*  \brief       reset the Framebuffer
*  \param       dataPtr String to scroll across
*  \param       fb Pointer to the frame buffer array
*  \exception   none
*  \return      length of frame buffer
***********************************************************************/             
function ShowDateAndTime(){

    var today = new Date();
    var month = today.getMonth();
    var day = today.getDay();
    var year = today.getFullYear();
    var hour = today.getHours();
    var minute = today.getMinutes();
    var seconds = today.getSeconds();
    const options_date = {year: 'numeric', month: 'long', day: 'numeric' };
		const options_weekday = { weekday: 'long' };
    //document.getElementById('id_alarm_browser_width').innerHTML = 'Browser Height = ' + window.innerHeight;
    //document.getElementById('id_alarm_browser_heigth').innerHTML = 'Browser Width = ' + window.innerWidth;
    document.getElementById('id_header_date').innerHTML = today.toLocaleDateString('de-DE', options_date);
    document.getElementById('id_header_day_and_time').innerHTML = today.toLocaleDateString('de-DE', options_weekday) +" " + leadingzero(hour) + ':' + leadingzero(minute) + ":" + leadingzero(seconds);
    document.getElementById('id_header_user').innerHTML = "none";
	
	var timestamp = new Date().getTime();  
  
    var el = document.getElementById("testimg");  
  
    var queryString = "..\\Screenshot.png?t=" + timestamp;    
   
    el.src = queryString; 
	
}
 
 
 
 // ======== AFTER PAGE LOADS CALL YOUR SCRIPTS HERE =========

function Start(status) {

    // In most modern browsers the console should return:
    // "Browser Loader : Document : DOMContentLoaded : interactive"
    console.log(status);
    //Start Date and Time
    setInterval(ShowDateAndTime, 1000);
	
	// create a new timestamp     
	var timestamp = new Date().getTime();     
	var el = document.getElementById("testimg");     
	el.src = "..\\Screenshot.png?t=" + timestamp;  
    // add your script calls here...

}


// ======== JAVASCRIPT PAGE LOADER =========
// Stokely Web Page loader, 2022

if (document.readyState) {

    if (document.readyState === "complete" || document.readyState === "loaded") {

        Start("Browser Loader : Document : readyState : complete");

    } else {
       if (window.addEventListener) {

            // Never try and call 'DOMContentLoaded' unless the web page is still in an early loading state.
            if (document.readyState === 'loading' || document.readyState === 'uninitialized') {
                window.addEventListener('DOMContentLoaded', function () {

                // Most modern browsers will have the DOM ready after this state.
                if (document.readyState === "interactive") {
                    Start("Browser Loader : Document : DOMContentLoaded : interactive");

                    } else if (document.readyState === "complete" || document.readyState === "loaded") {
                        Start("Browser Loader : Document : DOMContentLoaded : complete");
                    } else {
                        Start("Browser Loader : Document : DOMContentLoaded : load");
                    }
                }, false);
            } else {
// FALLBACK LOADER : If the readyState is late or unknown, go ahead and try and wait for a full page load event. Note: This function below was required for Internet Explorer 9-10 to work because of non-support of some readyState values! IE 4-9 only supports a "readyState" of "complete".
                if (document.readyState === 'complete' || document.readyState === "loaded") {
                    Start("Browser Loader : Document : readyState : complete");
                } else {
                    window.addEventListener('load', function () {
                        Start('Browser Loader : Window : Event : load');
                    }, false);
                }
            }
        // If 'addEventListener' is not be supported in the browser, try the 'onreadystate' event. Some browsers like IE have poor support for 'addEventListener'.
        } else {
            // Note: document.onreadystatechange may have limited support in some browsers.
            if (document.onreadystatechange) {
                document.onreadystatechange = function () {
                    if (document.readyState === "complete" || document.readyState === "loaded"){
                        Start("Browser Loader : Document : onreadystatechange : complete");
                    } 
                    // OPTIONAL: Because several versions of Internet Explorer do not support "interactive" or get flagged poorly, avoid this call when possible.
                    //else if (document.readyState === "interactive") {
                    //Start("Browser Loader : Document : onreadystatechange : interactive");
                    //}
                }
            } else {
            // Note: Some browsers like IE 3-8 may need this more traditional version of the loading script if they fail to support "addeventlistener" or "onreadystate". "window.load" is a very old and very reliable page loader you should always fall back on.
                window.onload = function() {
                    Start("Browser Loader : Window : window.onload (2)");
                };
            }
        }
    }
} else {
// LEGACY FALLBACK LOADER. If 'document.readyState' is not supported, use 'window.load'. It has wide support in very old browsers as well as all modern ones. Browsers Firefox 1-3.5, early Mozilla, Opera < 10.1, old Safari, and some IE browsers do not fully support 'readyState' or its values. "window.load" is a very old and very reliable page loader you should always fall back on.
    window.onload = function () {
        Start("Browser Loader : Window : window.onload (1)");
    };
}