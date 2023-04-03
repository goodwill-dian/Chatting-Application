
const ws = new WebSocket('ws://127.0.0.1:8000/ac/')

ws.onmessage = function (e){
    var dataset = JSON.parse(e.data);
    var div = document.createElement("div");
    // div.innerHTML = dataset.username + " : " + dataset.message
    div.innerHTML = dataset.message
    document.querySelector("#id_message_send_input").value = "";
    document.querySelector("#id_chat_item_container").appendChild(div)

}

ws.onclose = function (e){
    console.log("Connected Closed.");
};

document.querySelector("#id_message_send_input").focus();
document.querySelector("#id_message_send_input").onkeyup = function (e){
    if (e.keyCode == 13) {
        document.getElementById('id_message_send_button').click();
    }
};

document.getElementById('id_message_send_button').onclick = function (e){
    var messageInput = document.getElementById("id_message_send_input").value;
    // ws.send(JSON.stringify({message:messageInput, username:"{{request.user.first_name}}"}));
    ws.send(JSON.stringify({message:messageInput}));
}