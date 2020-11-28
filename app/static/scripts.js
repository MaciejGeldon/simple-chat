$(document).ready(function() {
    var url = "http://" + document.domain + ":" + location.port;
    console.log("url : " + url);

    var socket = io.connect(url);

    socket.on('client_count', function(msg) {
        console.log('got client count : ' + msg.count)
        $("#connected").html(msg.count);
    });


    $('form').submit(function(e){
        console.log('emit message')
        socket.emit('chat_message', $('#m').val());
        $('#m').val('');
        return false;
    });


    socket.on('chat_message', function(msg){
        var decoder = new TextDecoder('utf-8');
        parsed = JSON.parse(decoder.decode(msg));
        $('#messages').append($('<li>').text(""+parsed.name+":"+parsed.msg));
        window.scrollTo(0, document.body.scrollHeight);
    });
});