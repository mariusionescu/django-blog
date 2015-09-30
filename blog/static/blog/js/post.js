/**
 * Created by marius on 07/09/15.
 */

var editors = [];

window.onload = function () {
    var addEditor = function () {
        django.jQuery('.vLargeTextField').each(function(index, elem){
            var textarea = django.jQuery(this)[0];
            if(textarea.id.indexOf('__prefix__') == -1) {

                if (django.jQuery.inArray(index, editors) == -1) {
                    CodeMirror.fromTextArea(elem, {
                        lineNumbers: true,
                        theme: 'ambiance',
                        mode: 'xml',
                        lineWrapping: true
                    });
                    editors.push(index)
                }
            }
        });
    };

    addEditor();

    django.jQuery(".add-row").click(function () {
        addEditor()
    })
};
