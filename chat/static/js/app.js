const roomName = JSON.parse(document.getElementById('room-name').textContent);
const conservation = document.getElementById('conversation');
//bağlantı
const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
);
//websocketten veri geldiğinde çalışır
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    var message = `<div class="row message-body">
<div class="col-sm-12 message-main-sender">
<div class="sender">
<div class="message-text">
${data.message}
</div>
<span class="message-time pull-right">
Sun
</span>
</div>
</div>
</div>`
conservation.innerHTML += message;
};
//websoketten bağlantısı kapandığında 
chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};
// sayfa açıldığında inputa odaklar
document.querySelector('#comment').focus();
document.querySelector('#comment').onkeyup = function(e) {
    if (e.key === 13) {  // enter, return
        document.querySelector('#send').click();
    }
};
// mesajın json'a çevrilip gönderilmesi işini yapar
document.querySelector('#send').onclick = function(e) {
    const messageInputDom = document.querySelector('#comment');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
};