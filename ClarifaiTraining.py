from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage



app = ClarifaiApp("MdOfa_EpFLbvDaviwQs-7gTfWcRN3ZSqq4XXYK5e", "NhuichfJW4_WTV1Uin7KepgQuzjOo2DoCAtaVytn")
app.auth.get_token()

 #adding images
for i in range(12):
	local_filename = str(i) + ".jpeg"
	app.inputs.create_image_from_filename(local_filename, concepts=['Rithika'])

model = app.models.create('rithika', concepts=['Rithika'])
print(model)
model = app.models.get("robota")
model.train()

