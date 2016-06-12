// Setup i-frame fields for BrainTree form
$(function() {
    braintree.setup(
        "{{ request.session.braintree_client_token }}",
        "custom",
        {
            id: "creditcard_form",
            hostedFields: {
                number: {
                    selector: "#cc_number"
                },
                expirationDate: {
                    selector: "#cc_expiration_date"
                },
                cvv: {
                    selector: "#cc_verification_code"
                },
            },
        }
    );
});
