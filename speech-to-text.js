export default (request) => { 
    const kvstore = require('kvstore');
    const xhr = require('xhr');
    const Buffer = require('buffer').Buffer;
    
    console.log(request);
    var auth = new Buffer('CLIENT_ID' + ':' + 'CLIENT_SECRET').toString('base64');
    const http_options = {
        "method": "POST",
        "headers": {
            'Authorization': 'Basic ' + auth,
            "Content-Type": "audio/wav"
         },
         "data": request.message.data,
        
    };
    
    console.log('request',request); // Log the request envelope passed 
    return xhr.fetch(url, http_options).then((x) => {
        const body = JSON.parse(x.body);
        console.log(body);
        return request.ok();
    });
}
