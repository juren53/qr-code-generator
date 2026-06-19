# Testing use of QR codes for Museum artifacts

**Thread:** Jim Uren, Shelly Franklin, Clay, Kim
**Dates:** May 20–22, 2025

---

## JU → Clay, Kim, Shelly — May 20, 2025, 10:20 AM

Greetings All - -

Yesterday at the Museum, Shelly suggested I look into implementing QR codes to provide contextual information on Museum artifacts. Below are the first two tests that link to images I uploaded to the Internet Archive and populated with some metadata -- it's all placeholder info that can be updated by "professionals".

You will need to click on each QR image and then shoot the QR code with your cell phone camera and a link will appear that should take you to an image and description on the IA site.

BTW - - use of the Internet Archive is free and open source. The interface is somewhat clunky but it works.

Also, here is an example of a collection I built for the Truman Home that has a small portion of Mr. Truman's record collection: https://archive.org/details/trumanhomemusic

We could do something like this for the Museum. Lots to talk about and plan to implement it with QR codes but I think it is very doable. Let me know what you think,

Jim

**Attachments:** QR_ships-bell.png, QR_bridge-clock.png

---

## Shelly Franklin → Jim — May 21, 2025, 10:26 AM

Jim, this is fantastic! Exactly what I was imagining for items currently on display with no info label. Thanks for doing these two as a test case. I would personally be in favor of exploring more possibilities here.

And the record collection info is very cool - someone stumbling across one piece like that online could compel them to visit the Truman home and Library, just to see what else is there. That could work in the museum's favor as well.

Thanks again!
shelly

---

## JU → Clay, Kim, Shelly — May 22, 2025, 11:14 AM

*(This is Jim's final, complete message on the thread — an earlier truncated send at 10:53 AM was retracted.)*

I was a little surprised—and encouraged—by how easy it was to get these two examples working. The technology has matured to the point where we should be able to implement this at WHM with relatively little friction.

Now, we're at that stage where "the devil's in the details." Details like:

- Is the Internet Archive the right backend data store to serve WHM artifact data to the public? (There's evidence in favor — many museums around the world use IA — but it's not the only option.)
- How should we structure the backend data?
- How do we implement a WHM-specific artifact numbering system?
- How do we unobtrusively display QR codes in the Museum?
- What's the best way to display them?
- What's the ideal size for visibility and scannability?
- ...and many more implementation details like these.

**Quick note on testing:** When I printed the test QR codes, I was pleasantly surprised at how much faster my phone recognized the printed versions compared to those displayed on a computer screen. I was even able to shrink them to under 2 cm (about 0.75 inches), and my phone still scanned them successfully.

We'll definitely need to conduct more thorough testing in the Museum to determine the ideal size and display options.

So far, my limited testing suggests some important trade-offs involving:

- QR code size
- Lighting conditions
- Phone hardware:
  - Age
  - OS version
  - Camera resolution

I could go on, but you get the idea — it's worth taking our time to get this right for the Museum environment. That's it for now. Let's talk more about it next Monday at the Museum.

Best,
Jim
