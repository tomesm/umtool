from subprocess import check_output



cmd = 'dscl . -list /groups PrimaryGroupID | grep staff | tr -s [:space:]'
out = check_output([cmd], shell=True)


res = out.decode('UTF-8').strip('\n').split(' ')

cmd = "dscl . -list /Users UniqueID|awk '{{print $2}}'|sort -ug|tail -1"
out = check_output([cmd], shell=True)
        # Increment the current max user
        #
# print(str(int(out.decode('UTF-8').strip('\n')) + 1))

out = check_output(['groups', 'martin'], shell=True)

print(out.decode('UTF-8').strip('\n').split(' '))

