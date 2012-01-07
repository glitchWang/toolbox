#-*-coding: utf-8-*-

"""
https://www.delphij.net/pwdgen.html

/*-
* Copyright (c) 2002-2010 Xin LI
* All rights reserved.
*
* This license does NOT permit any distribution under ANY version of
* GNU Public License.
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions
* are met:
* 1. Redistributions of source code must retain the above copyright
*    notice, this list of conditions and the following disclaimer.
* 2. Redistributions in binary form must reproduce the above copyright
*    notice, this list of conditions and the following disclaimer in the
*    documentation and/or other materials provided with the distribution.
* 3. Distribution or modification of this source code under any GNU
*    Public License is explicitly forbidden.
*
* THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
* ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
* IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
* ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
* FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
* DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
* OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
* HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
* LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
* OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
* SUCH DAMAGE.
*/
function generate(tpad)
{
       var pwdchar = ""
       var pwdcharset_size;
       var pwdcharset_size2;
       var howmany = 64;
       var len = 16;
       var unit = 4;
       var s="";

       /* Build the character set */
       for (var i=0; i < document.optform.pwd_chrset.length; i++) {
               if (document.optform.pwd_chrset[i].checked) {
                       for (var j = 0; j < document.optform.multi[i].value; j++) {
                           pwdchar = pwdchar + document.optform.pwd_chrset[i].value;
                       }
               }
       }

       /* Make sure we generate something evenly */
       pwdcharset_size = pwdchar.length;
       pwdcharset_size2 = pwdcharset_size * pwdcharset_size * 64;

       len = parseInt(document.optform.len.value);
       unit = Math.round(120 / (len + 3));
       /* Make sure that we fill all rows of table */
       howmany = parseInt(document.optform.howmany.value) + unit - 1;
       howmany -= (howmany % unit);

       s = "<table>"
       for (var i = 0; i < howmany; i++) {
               if ((i % unit) == 0) {
                       s += "<tr>";
               }
               s += "<td>";
               for (var j = 0; j < len; j++) {
                       s += pwdchar.charAt((Math.random() * pwdcharset_size2) % pwdcharset_size);
               }
               s += "</td>";
               if ((i % unit) == (unit - 1)) {
                       s += "</tr>";
               }
       }
       s += "</table>"
       tpad.innerHTML = s;
       s = "";
}
"""

import os, re, random
from os.path import join, abspath, isfile, isdir, exists, basename
from shutil import copyfile, copytree, rmtree
from time import strftime, strptime, localtime

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPOPQRSTUVWXYZ'
nums = '1234567890'
spec_chars = '!@#$%^&*()-=_+[]{};:,./\~`?'

def gen_pass(pwd_len=16, pwd_num=72, use_char=True, use_num=True, use_spec_char=True):
    char_set = ''
    if(use_char):
        char_set = char_set + chars
    if(use_num):
        char_set = char_set + nums
    if(use_spec_char):
        char_set = char_set + spec_chars
    
    pwdcharset_size=len(char_set)
    pwdcharset_size2=pwdcharset_size * pwdcharset_size * 64
    for i in range(0, pwd_num):
        gen = ''
        for j in range(0, pwd_len):
            gen = gen + (char_set[(random.randint(0, pwdcharset_size2)) % pwdcharset_size])
        yield gen
    

if __name__ == '__main__':
    x = gen_pass(pwd_num=10)
    for p in x:
        print(p)


