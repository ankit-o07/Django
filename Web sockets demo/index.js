
const http = require("http")
const webScoketServer = require("websocket").server
const httpserver = http.createServer((req,res) =>{

    console.log("We have received a request");
})


const websocket = new webScoketServer({
    "httpServer":httpserver
})

websocket.on("request",request =>{

    connection = request.accept(null,request.origin)
    connection.on("open",()=>console.log("Opened!!!"))
    connection.on("close",()=>console.log("Close!!!"))
    connection.on("message",message=>{
        console.log(`Recevived message ${message.utf8Data}`);
    })
    sendevery5second();
})

httpserver.listen(8080, () => 
    console.log("My server is listening on port 8080")
    )
function sendevery5second(){
    connevtion.send(`Message ${Math.random()}`);
    setTimeout(sendevery5second,5000);
    }