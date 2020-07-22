const venom = require('venom-bot');

venom.create().then((client) => start(client));

function start(client) {
    const zoom = process.argv[2]
    const pdf = process.argv[3]
    const id = process.argv[4]
    const password = process.argv[5]
    client.onMessage((message) => {
        switch (message.body.toLowerCase()) {
            case 'zoom':
                client.sendText(message.from, zoom);
                break;
            case 'pdf':
                client.sendText(message.from, pdf);
                break;
            case 'id':
                client.sendText(message.from, id);
                break;
            case 'senha':
                client.sendText(message.from, password);
                break;
            case 'password':
                client.sendText(message.from, password);
                break;
        }
    });
}
