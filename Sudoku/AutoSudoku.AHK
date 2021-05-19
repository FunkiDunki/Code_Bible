^g::
numbers := StrSplit(clipboard)
for i, element in numbers
{
	if(i != 1)
	{
		send {tab}
	}
	sleep 5
	send %element%
	sleep 5
}
send {enter}
return
