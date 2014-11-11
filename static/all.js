function onload() {
	//setInterval(updateTime, 1000);
}

function updateTime() { 
	// Initialize the Ajax request
	var xhr = new XMLHttpRequest();
	xhr.open('get', '/test-ajax');
	 
	// Track the state changes of the request
	xhr.onreadystatechange = function(){
	    // Ready state 4 means the request is done
	    if(xhr.readyState === 4){	     
	        if(xhr.status === 200){	     
            	document.getElementById("time").innerHTML = xhr.responseText;				
	        } else{
	            alert('Error: '+xhr.status); 
	        }
	    }
	}
	xhr.send(null);
}