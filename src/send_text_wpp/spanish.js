const venom = require("venom-bot");

venom.create().then((client) => start(client));

function start(client) {
    const zoom = process.argv[2];
    const pdf = process.argv[3];
    const id = process.argv[4];
    const password = process.argv[5];

    const msg = `Boa tarde\nLink do PDF de hoje: ${pdf}\nLink do Zoom vespertino: ${zoom}\nID da reunião: ${id}\nSenha: ${password}`;

    const PHONE_NUMBER = "";

    client.sendText(PHONE_NUMBER, msg);

    client.onMessage((message) => {
        switch (message.body.toLowerCase()) {
            case "zoom":
                client.sendText(message.from, zoom);
                console.log(`Zoom URL sucessfully sent to ${message.from}`);
                break;
            case "pdf":
                client.sendText(message.from, pdf);
                console.log(`PDF URL sucessfully sent to ${message.from}`);
                break;
            case "id":
                client.sendText(message.from, id);
                console.log(`ID sucessfully sent to ${message.from}`);
                break;
            case "senha":
                client.sendText(message.from, password);
                console.log(`Password sucessfully sent to ${message.from}`);
                break;
            case "password":
                client.sendText(message.from, password);
                console.log(`Password sucessfully sent to ${message.from}`);
                break;
        }
    });
}
