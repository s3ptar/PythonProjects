default_dataset = [
        {
            "target_system" : "volvo",
    				"timeout_fly_to_sys" : 120,
    				"target_list":[{
        				"battleship":1,
        				"interceptor":1,
        				"explorer":1,
        				"miner":0
    	}],
    	"num_of_target_kills":52,
      "num_of_repeats": 4,
    	"closed_kill_enable":1,
    	"cargo_modus_enabled":1,
      "task_enable":1
		},
    {
            "target_system" : "saab",
    				"timeout_fly_to_sys" : 120,
    				"target_list":[{
        				"battleship":1,
        				"interceptor":0,
        				"explorer":1,
        				"miner":1
    	}],
    	"num_of_target_kills":52,
      "num_of_repeats": 6,
    	"closed_kill_enable":1,
    	"cargo_modus_enabled":1,
      "task_enable":0
		},
];

var glb_var_tasknum;
/***********************************************************************
*! \fn          function LoadData(Tab)
*  \brief       load data into tab
*  \param       evt - event
*  \exception   none
*  \return      length of frame buffer
***********************************************************************/
function LoadData(Tab){

    var tasknum = 0;
    switch(Tab){
        case 'Task1':
            tasknum = 0;
            break;
        case 'Task2':
            tasknum = 1;
            break;
        case 'Task3':
            tasknum = 2;
            break;
        case 'Task4':
            tasknum = 3;
            break;
        case 'Task5':
            tasknum = 4;
            break;
        case 'Task6':
            tasknum = 5;
            break;
        default:
            return;
    }
    glb_var_tasknum = tasknum;

    document.getElementById("id_num_of_repeats").value = default_dataset[tasknum].num_of_repeats;
    document.getElementById("id_task_enable").checked  = default_dataset[tasknum].task_enable;

    for (var i = 0; i < document.getElementById("id_system").options.length; i++) {
        if (document.getElementById("id_system").options[i].text.toLowerCase() == default_dataset[tasknum].target_system.toLowerCase()) {
            document.getElementById("id_system").options[i].selected = true;
            break;
        }
		}
    document.getElementById("id_flight_time").value = default_dataset[tasknum].timeout_fly_to_sys;

    document.getElementById("id_num_of_targets").value = default_dataset[tasknum].num_of_target_kills;
    document.getElementById("id_target_battleship").checked  = default_dataset[tasknum].target_list[0].battleship;
    document.getElementById("id_target_explorer").checked  = default_dataset[tasknum].target_list[0].interceptor;
    document.getElementById("id_target_interceptor").checked  = default_dataset[tasknum].target_list[0].explorer;
    document.getElementById("id_target_miner").checked  = default_dataset[tasknum].target_list[0].miner;

    document.getElementById("id_return_full_cargo").checked  = default_dataset[tasknum].cargo_modus_enabled;
    document.getElementById("id_closed_target").checked  = default_dataset[tasknum].closed_kill_enable;
}

/***********************************************************************
*! \fn          function SaveData(evt)
*  \brief       save input data to variable
*  \param       evt - event
*  \exception   none
*  \return      length of frame buffer
***********************************************************************/
function SaveData(evt){

    var tmp_dataset;
    tmp_dataset = [
        {
            "target_system" : document.getElementById("id_system").value,
    				"timeout_fly_to_sys" : document.getElementById("id_flight_time").value,
    				"target_list":[{
        				"battleship":document.getElementById("id_target_battleship").checked ? 1 : 0,
        				"interceptor":document.getElementById("id_target_interceptor").checked ? 1 : 0,
        				"explorer":document.getElementById("id_target_explorer").checked ? 1 : 0,
        				"miner":document.getElementById("id_target_miner").checked ? 1 : 0,
    	}],
    	"num_of_target_kills":document.getElementById("id_num_of_targets").value,
      "num_of_repeats": document.getElementById("id_num_of_repeats").value,
    	"closed_kill_enable":document.getElementById("id_closed_target").checked ? 1 : 0,
    	"cargo_modus_enabled":document.getElementById("id_return_full_cargo").checked ? 1 :0
		}
];

 //console.log(tmp_dataset);
 //console.log(glb_var_tasknum);

    default_dataset[glb_var_tasknum].num_of_repeats = document.getElementById("id_num_of_repeats").value;
    default_dataset[glb_var_tasknum].task_enable = document.getElementById("id_task_enable").checked;

    default_dataset[glb_var_tasknum].target_system = document.getElementById("id_system").value;
    default_dataset[glb_var_tasknum].timeout_fly_to_sys = document.getElementById("id_flight_time").value;

    default_dataset[glb_var_tasknum].num_of_target_kills = document.getElementById("id_num_of_targets").value;
    default_dataset[glb_var_tasknum].target_list[0].battleship = document.getElementById("id_target_battleship").checked;
    default_dataset[glb_var_tasknum].target_list[0].interceptor = document.getElementById("id_target_explorer").checked;
    default_dataset[glb_var_tasknum].target_list[0].explorer = document.getElementById("id_target_interceptor").checked;
    default_dataset[glb_var_tasknum].target_list[0].miner = document.getElementById("id_target_miner").checked;

    default_dataset[glb_var_tasknum].cargo_modus_enabled = document.getElementById("id_return_full_cargo").checked;
    default_dataset[glb_var_tasknum].closed_kill_enable = document.getElementById("id_closed_target").checked;

}

/***********************************************************************
*! \fn          openTab(evt, Tab)
*  \brief       event function
*  \param       evt - event
*  \exception   none
*  \return      length of frame buffer
***********************************************************************/
function openTab(evt, Tab) {
    var i, tabcontent, tablinks;

    if (Tab == "General") {
        document.getElementById("id_task_div").style.display = "none";
        document.getElementById("id_general_task").style.display = "block";
    }else{
        document.getElementById("id_task_div").style.display = "block";
        document.getElementById("id_general_task").style.display = "none";
    }

    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    evt.currentTarget.className += " active";
    LoadData(Tab);
}

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
    const options_date = {year: 'numeric', month: 'numeric', day: 'numeric' };
		const options_weekday = { weekday: 'long' };
    //document.getElementById('id_alarm_browser_width').innerHTML = 'Browser Height = ' + window.innerHeight;
    //document.getElementById('id_alarm_browser_heigth').innerHTML = 'Browser Width = ' + window.innerWidth;
    var timestr = leadingzero(hour) + ':' + leadingzero(minute) + ":" + leadingzero(seconds) + " " + today.toLocaleDateString('de-DE', options_date);
    //console.log( today.toLocaleDateString('de-DE', options_date));


}

/***********************************************************************
*! \fn          get_data_from_srv()
*  \brief       AFTER PAGE LOADS CALL YOUR SCRIPTS HERE
*  \param       status - status from page load dunction
*  \exception   none
*  \return      none
***********************************************************************/
function get_data_from_srv(){

    //var sliderValue = document.getElementById("pwmSlider").value;
    //document.getElementById("textSliderValue").innerHTML = sliderValue;
    //console.log(sliderValue);
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/update?"+JSON.stringify(default_dataset), true);
    xhr.send();

}


/***********************************************************************
*! \fn          function Start(status)
*  \brief       AFTER PAGE LOADS CALL YOUR SCRIPTS HERE
*  \param       status - status from page load dunction
*  \exception   none
*  \return      none
***********************************************************************/
function Start(status) {

    // In most modern browsers the console should return:
    // "Browser Loader : Document : DOMContentLoaded : interactive"
    console.log(status);
    //Start Date and Time
    setInterval(ShowDateAndTime, 1000);
    setInterval(get_data_from_srv, 10000);
    //openTab("", "General")
    document.getElementById("id_task_div").style.display = "none";
    document.getElementById("id_general_task").style.display = "block";

    //test function for log tab
    //setInterval(generate_log_data, 10000);
    // add your script calls here...
    //hide all elements, expect home



}

/***********************************************************************
*! \fn          page load
*  \brief       JAVASCRIPT PAGE LOADER
*  \author      Stokely Web Page loader, 2022
*  \param       none
*  \exception   none
*  \return      status from loaded page
***********************************************************************/
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
            // Note: Some browsers like IE 3-8 may need this more traditional version of the loading script if they fail to support "addeventlistener" or "onready             state". "window.load" is a very old and very reliable page loader you should always fall back on.
                window.onload = function() {
                    Start("Browser Loader : Window : window.onload (2)");
                };
            }
        }
    }
} else {
    // LEGACY FALLBACK LOADER. If 'document.readyState' is not supported, use 'window.load'. It has wide support in very old browsers as well as all modern ones.     Browsers Firefox 1-3.5, early Mozilla, Opera < 10.1, old Safari, and some IE browsers do not fully support 'readyState' or its values. "window.load" is a very     old and very reliable page loader you should always fall back on.
    window.onload = function () {
        Start("Browser Loader : Window : window.onload (1)");
    };
}



