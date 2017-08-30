export default (request) => { 
    const kvstore = require('kvstore');
    const xhr = require('xhr');
    
    const http_options = {
        "method": "GET",
        "headers": {
            "Authorization": "Basic {IBM_TOKEN}",
         },
         
        
    }

    console.log('request',request.message); // Log the request envelope passed 
    return xhr.fetch("https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2016-05-19&text="+escape(request.message), http_options).then((x) => {
        //console.log(JSON.parse(x.body).document_tone);
        var arr = JSON.parse(x.body).document_tone.tone_categories[0].tones;
        console.log(arr);
        var max = arr[0];
        for (var i = 1; i < 5; i++){
            if (max.tone_name != 'Joy' && arr[i].score > max.score){
                max = arr[i];
            }
        }
        var emotion;
        if (max.tone_name == 'Joy'){
            emotion = "happy";
        } else if (max.tone_name == 'Sadness'){
            emotion = "sad";
        } else if (max.tone_name == 'Anger'){
            emotion = "angry";
        } else if (max.tone_name == 'Disgust'){
            emotion = "disgusted";
        } else if (max.tone_name == 'Fear'){
            emotion = "scared";
        }
        var level;
        if (max.score > 0.80){
            level = "very";
        } else if (max.score > 0.60){
            level = "somewhat";
        } else {
            level = "slightly";
        }
        var string = "Your student is feeling " + level + " " + emotion + ". You should go help them out.";
        
        const http_options3 = {
            "method": "POST",
            "headers": {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            "body": "api_key={NEXMO_API_KEY}&api_secret={NEXMO_API_SECRET}&to={TO_PHONE_NUMBER}&from={FROM_PHONE_NUMBER}&text="+string
        }
        return xhr.fetch("https://rest.nexmo.com/sms/json", http_options3).then((z) => {
            console.log(z);
            return request.ok();
        });
    }); 
}
