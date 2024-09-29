const roomName = JSON.parse(document.getElementById('room-name').textContent);
const user = JSON.parse(document.getElementById('user').textContent);
document.getElementById('hiddeninput').addEventListener('change',handleFileSelect,false)
function handleFileSelect(){
    var file = document.getElementById('hiddeninput').files[0]
    getBase64(file)
}
function getBase64(file){
    var reader = new FileReader();
    reader.readAsDataURL(file)

    reader.onload = function(){
        chatSocket.send(JSON.stringify({
            'type_control':"image",
            'message':reader.result
        }))
    }
}
const conservation = document.getElementById('conversation');
//bağlantı
const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
);
//websocketten veri geldiğinde çalışır
chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    const message_type = data.type_control;
    if (message_type === "text"){
        var message = data.message
    }
    else if(message_type === "image"){
        var message = `img src="${data.message}" width="250" heigth="250">`
    }
    if(user==data.user){
        var message = `<div class="row message-body">
        <div class="col-sm-12 message-main-sender">
        <div class="sender">
            <div class="message-text">
            ${message}
            </div>
            <span class="message-time pull-right">
            ${data.date}
            </span>
        </div>
        </div>
    </div>` 
    }
    else{
        var message = `<div class="row message-body">
        <div class="col-sm-12 message-main-receiver">
        <div class="receiver">
            <div class="message-text">
            ${message}
            </div>
            <span class="message-time pull-right">
            ${data.date}
            </span>
        </div>
        </div>
    </div>` 
    }
    
    conservation.innerHTML += message;
};
//websoketten bağlantısı kapandığında 
chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpectedly');
};
// sayfa açıldığında inputa odaklar
document.querySelector('#comment').focus();
document.querySelector('#comment').onkeyup = function (e) {
    if (e.key === 13) {  // enter, return
        document.querySelector('#send').click();
    }
};
// mesajın json'a çevrilip gönderilmesi işini yapar
document.querySelector('#send').onclick = function (e) {
    const messageInputDom = document.querySelector('#comment');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'type_control':"text",
        'message': message
    }));
    messageInputDom.value = '';
};