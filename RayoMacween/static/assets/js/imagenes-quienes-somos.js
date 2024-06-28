$(document).ready(function() {
    const llave = 'BQbqkqbcCD1Or2vHhrMj49tEDrgCS24MBQ6h_Uv1WIM'; 
    const fotos = [
        { id: 'l6_FAGuqfSA', element: '#mecanico' },
        { id: 'EJr3XkHdBm0', element: '#mecanico-2' },
        { id: 'NLOmgkbouSk', element: '#mecanico-3' },
        {id:'9fWL9CAluSA', element: '#mecanico-4'},
        {id:'t59Y-XgI4oI', element: '#mecanico-5'},
        {id: 'eC62S_EK5GM', element: '#mecanico-6'}
    ];

    fotos.forEach(foto => {
        $.ajax({
            url: `https://api.unsplash.com/photos/${foto.id}`,
            method: 'GET',
            data: {
                client_id: llave
            },
            success: function(data) {
                const imageUrl = data.urls.regular;
                $(foto.element).attr('src', imageUrl);
                console.log('Photo ID:', data.id);
            },
            error: function(xhr, status, error) {
                console.error('Error:', status, error);
            }
        });
    });
});
