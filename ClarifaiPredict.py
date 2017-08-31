from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import base64

app = ClarifaiApp("MdOfa_EpFLbvDaviwQs-7gTfWcRN3ZSqq4XXYK5e", "NhuichfJW4_WTV1Uin7KepgQuzjOo2DoCAtaVytn")
app.auth.get_token()

model = app.models.get('NegativeRithika')
image = ClImage(file_obj=open('./ab.jpg', 'rb'))

print(model.predict([image]))