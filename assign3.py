{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "139df7cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a word:-\"I Am A Great Indain Citizen\"\n",
      "Upper Case Letters:- 6\n",
      "Lower Case Letters:- 16\n"
     ]
    }
   ],
   "source": [
    "def up_low(string):\n",
    "    up=0\n",
    "    low=0\n",
    "    for i in string:\n",
    "        if i.isupper():\n",
    "            up+=1\n",
    "        elif i.islower():\n",
    "            low+=1\n",
    "    print(\"Upper Case Letters:-\",up)\n",
    "    print(\"Lower Case Letters:-\",low)\n",
    "s=input(\"Enter a word:-\")\n",
    "up_low(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1407e341",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 5, 8, 3]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Write a Python function that takes a list and returns a new list with unique elements:\n",
    "def unique_list(l):\n",
    "    newlist=[]\n",
    "    for i in (l):\n",
    "        if i not in newlist:\n",
    "            newlist.append(i)\n",
    "    return newlist\n",
    "unique_list([2,5,8,2,3,8,5,2])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d26ea6ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Even number is:\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[2, 4, 6, 8]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Write a Python program to print the even numbers from a given list:\n",
    "def even_num(list):\n",
    "    even=[]\n",
    "    for i in (list):\n",
    "        if i%2==0:\n",
    "            even.append(i)    \n",
    "    return even\n",
    "print(\"Even number is:\")\n",
    "even_num([2,4,6,8,9,7,5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "0745e4c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The given word is palindrome\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'madam'"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Write a Python function that checks whether a passed string is palindrome or not\n",
    "def palindrome(p):\n",
    "    s=p[::-1]\n",
    "    if s==p:\n",
    "        print(\"The given word is palindrome\")\n",
    "        return s\n",
    "    else:\n",
    "        print(\"The given word is not palindrome\")\n",
    "        return s\n",
    "palindrome(\"madam\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "56d3ab9f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23bd953e",
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
