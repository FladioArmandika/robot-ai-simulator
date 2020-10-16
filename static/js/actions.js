var stream = document.getElementById( "stream" );
var btnAnalyze = document.getElementById( "btn-capture" );
var capture = document.getElementById( "capture" );

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

// AUDIO
// const recorder = document.getElementById('recorder');
// const player = document.getElementById('player');

// recorder.addEventListener('change', function(e) {
//     const file = e.target.files[0];
//     const url = URL.createObjectURL(file);
//     // Do something with the audio file.
//     player.src = url;
// });

// END AUDIO

var playArea = document.getElementById( "play-area" );

btnAnalyze.addEventListener( "click", analyze );
function analyze() {

    // RECORD VIDEO
    var ctx = capture.getContext( '2d' );
    var img = new Image();
    ctx.drawImage( stream, 0, 0, capture.width, capture.height );
    img.src		= capture.toDataURL( "image/png" );
    img.width	= 240;

    var formdata = new FormData();
    formdata.append('video', img);

    // SEND TO SERVER
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://localhost:5000/analyze", true);
    playArea.style.opacity = 0.4;
    xhttp.send(formdata);
    setTimeout(function(){ 
        playArea.style.opacity = 1;
        alert('ANALYZE DONE')
    }, 1000);
    
    // alert('DONE');
}