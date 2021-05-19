^g::
numbers := StrSplit(clipboard)
for i, element in numbers
{
	if(i != 1)
	{
		send {tab}
	}
	sleep 1
	send %element%
	sleep 1
}
send {enter}
return
