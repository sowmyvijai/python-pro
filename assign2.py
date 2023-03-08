{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00eb4e86",
   "metadata": {},
   "outputs": [],
   "source": [
    "# write a python function to find the maximum numbers:\n",
    "def largest(num1,num2,num3):\n",
    "    return max(num1,num2,num3)\n",
    "largest(34,25,42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "1efb3240",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ecneicsatad'"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Write a python function to reverse a string:\n",
    "def reverse(string):\n",
    "    reverse=string[::-1]\n",
    "    return reverse\n",
    "reverse(\"datascience\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "10d4a180",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "350 is in a given range\n"
     ]
    }
   ],
   "source": [
    "#Write a Python function to check whether a number falls in a given range:\n",
    "def check_range(s,e,n):\n",
    "    if s<=n<=e:\n",
    "        print(n,\"is in a given range\")\n",
    "    else:\n",
    "        print(n,\"is not in a given range\")\n",
    "    \n",
    "check_range(100,500,350)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1382424a",
   "metadata": {},
   "outputs": [],
   "source": [
    "  #Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters\n",
    "def upp_low(s):\n",
    "    up=0\n",
    "    low=0\n",
    "    for i in (s):\n",
    "        if i.isupper():\n",
    "            up+=1\n",
    "        elif i.islower():\n",
    "            low+=1\n",
    "    print(\"Upper case letters in given string are\",up)\n",
    "    print(\"lower case letters in given string are\",low)\n",
    "s=input(\"Enter a Word:\")\n",
    "upp_low(s)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d31c3f46",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26d3a549",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c921aef9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8373e427",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
