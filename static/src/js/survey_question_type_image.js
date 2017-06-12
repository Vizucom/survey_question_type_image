odoo.define('survey_question_type_image.survey_question_type_image', function (require) {

    'use strict';

    var prefillController;
    var $surveyForm;

    // Pre-filling of the form with previous answers
    function custom_prefill(){

        if (! _.isUndefined(prefillController)) {
            var prefill_def = $.ajax(prefillController, {dataType: "json"})
                .done(function(json_data){
                    _.each(json_data, function(value, key){
                        // prefill of text/number/date boxes
                        var input = $surveyForm.find(".form-control[name=" + key + "][type!='file']");
                        input.val(value);

                        // special case for comments under multiple suggestions questions
                        if (_.string.endsWith(key, "_comment") &&
                            (input.parent().hasClass("js_comments") || input.parent().hasClass("js_ck_comments"))) {
                            input.siblings().find('>input').attr("checked","checked");
                        }

                        // checkboxes and radios
                        $surveyForm.find("input[name^=" + key + "][type!='text'][type!='file']").each(function(){
                            $(this).val(value);
                        });

                        // image inputs
                        $surveyForm.find("input[name=" + key + "][type='file']").each(function(){
                            // Show the previously uploaded image in preview div
                            var bgUrl = 'url("/web/image/survey.user_input_line/' + value + '/value_image")';
                            $(this).closest("#image-preview").css("background-image", bgUrl);
                        });
                    });
                })
                .fail(function(){
                    console.warn("[survey] Unable to load prefill data");
                });
            return prefill_def;
        }
    }

    $(document).ready(function() {

        $surveyForm = $('.js_surveyform')
        // Use the custom controller and call the custom prefill function
        prefillController = $surveyForm.attr("data-custom-prefill");
        custom_prefill();

        // Init the image preview widget
        $.uploadPreview({
          input_field: "#image-upload",
          preview_box: "#image-preview",
          label_field: "#image-label",
          label_default: '<span class="fa fa-upload"/>',
          label_selected: '<span class="fa fa-upload"/>',
          no_label: false
        });
    });
});
