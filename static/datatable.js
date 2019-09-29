$(document).ready(function() {
    mysql_return = mysql
    
    $('#example tfoot th').each( function () {
        var title = $(this).text();
        $(this).html( '<input type="text" placeholder="Search '+title+'" />' );
    } );

    var table = $('#example').DataTable( {
        data: mysql_return,
        columns: [
            { title: "Movie Title" },
            { title: "Movie Year" },
            { title: "Movie Rating" },
            { title: "Movie Resolution" },
            { title: "Movie Container" },
            { title: "Movie Director" },
            { title: "Movie Genre" }
        ]
    } );

    table.columns().every( function () {
        var that = this;
 
        $( 'input', this.footer() ).on( 'keyup change clear', function () {
            if ( that.search() !== this.value ) {
                that
                    .search( this.value )
                    .draw();
            }
        } );
    } );
} );