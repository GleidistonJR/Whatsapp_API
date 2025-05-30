import os
import traceback

from services import EvolutionAPI


# instanciando class
evo_client = EvolutionAPI()

numero = 2245
message = f'Hello Word! {numero}.'

evo_client.send_message(
    number=os.getenv('EVO_PHONE_DEST'),
    text=message,
)

messageImage = 'Teste enviando img'

print(
    evo_client.send_image(
        number=os.getenv('EVO_PHONE_DEST'),
        text=messageImage,
        image='https://images.vexels.com/media/users/3/166477/isolated/lists/9bb722f0e85ddbc1ce0f064534fd2311-icone-da-linguagem-de-programacao-python.png',
    )
)