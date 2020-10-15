var stream = document.getElementById( "stream" );
var btnAnalyze = document.getElementById( "btn-capture" );

var cameraStream = null;

// Start Streaming
function startStreaming() {
    var mediaSupport = 'mediaDevices' in navigator;
    if( mediaSupport && null == cameraStream ) {
        navigator.mediaDevices.getUserMedia( { video: true } )
        .then( function( mediaStream ) {
            cameraStream = mediaStream;
            stream.srcObject = mediaStream;
            stream.play();
        })
        .catch( function( err ) {
            console.log( "Unable to access camera: " + err );
        });
    } else {
        alert( 'Your browser does not support media devices.' );
        return;
    }
}

startStreaming();

var playArea = document.getElementById( "play-area" );

btnAnalyze.addEventListener( "click", analyze );
function analyze() {
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "http://localhost:5000/analyze", true);
    playArea.style.opacity = 0.4;
    xhttp.send();
    setTimeout(function(){ 
        playArea.style.opacity = 1;
        alert('ANALYZE DONE')
    }, 1000);
    
    // alert('DONE');
}