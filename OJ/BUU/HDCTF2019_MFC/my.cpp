#include <stdio.h>
#include <Windows.h>

int main()
{
	HWND h = FindWindowA(NULL, "Flag就在控件里");
	if (h)
	{
		SendMessage(h, 0x464, 0, 0);
		printf("success");
	}
	else
		printf("fail");

	return 0;
}