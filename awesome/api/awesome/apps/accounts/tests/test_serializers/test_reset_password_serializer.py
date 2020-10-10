from awesome.apps.accounts.api.v1.serializers.password import ResetPasswordSerializer


def test_save(mocker):
    email = "jane@example.com"
    serializer = ResetPasswordSerializer(data={"email": email})
    mocked_send_reset_password_link = mocker.patch.object(serializer.password_service, "send_reset_password_link")

    serializer.is_valid()
    serializer.save()

    assert mocked_send_reset_password_link.called_once_with(email)
