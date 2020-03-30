$('.delete').click((event) => {

    const btn = event.currentTarget;
    const url = btn.attributes.link.nodeValue;
    $('#yes-delete').attr('href', url);

} );
