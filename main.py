import requests
from bs4 import BeautifulSoup

# URL a scrapear
#Usar variable para el path trayendola del front

path = 'contacto'
url = f'https://www.personal.com.ar/{path}'

# HTTP GET url
response = requests.get(url)

# Crear obj BeautifulSoup con el contenido HTML de la página
soup = BeautifulSoup(response.content, 'html.parser')

# Dicc para filtro de data-attributes
desired_data_attributes = ['data-ui-section', 'data-ui-element', 'data-component-name', 'data-ui-action', 'data-ui-contact','data-ui-section-1','data-ui-section-2', 'data-landing-name']

# Encontrar todos los elementos que contienen atributos que comienzan con "data- y pasen el filtro"
elements_with_data_attributes = soup.find_all(
    lambda tag: any(
        attr.startswith('data-') and (attr in desired_data_attributes)
        for attr in tag.attrs.keys()
    )
)

counter = 0


# Iterar sobre los elementos encontrados
for element in elements_with_data_attributes:
    # Obtener los nombres de los atributos que comienzan con "data-"
    attribute_names = [
        name for name in element.attrs.keys()
        if name.startswith('data-') and (name in desired_data_attributes)
    ]

    # Obtener el identificador único (ID) del elemento, si existe
    element_id = element.get('id')

    # Obtener la clase del elemento, si existe
    element_class = element.get('class')

    # Obtener los valores de los atributos de datos
    data_values = {attr: element.get(attr) for attr in attribute_names}

    # Construir la descripción del elemento con los atributos, clase, ID y valores de atributos de datos
    description = f"Elemento: <{element.name}>"
    # if attribute_names:
        # description += f", DA: {', '.join(attribute_names)}"
    if element_class:
        description += f" || Class: {', '.join(element_class)}"

    if element_id:
        description += f" || ID: {element_id}"

    if data_values:
        description += f" || DA: {data_values}"

    
    archive = open('DA.txt', 'a', encoding = 'utf-8')
    archive.write(f"{description} \n\n")
    archive.close()
    print(description)

    counter += 1

print(f"Hay {counter} elementos con data-attributes")