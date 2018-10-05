from Auth.models import Profile


class ProfileQuery:

    def get_user_by_id(self, pk):
        return Profile.objects.get(pk=pk)
