create table desktop (
model	varchar2(20)	not null,
price 	integer		not null,
cpu	integer 	not null,
primary key (model)
);

create table laptop (
model	varchar2(20)	not null,
price	integer 	not null,
cpu	integer		not null,
weight	integer		not null,
primary key (model)
);

create table hdtv (
model		varchar2(20)	not null,
price		integer 	not null,
screen_size	integer		not null,
primary key (model)
);

create table pdptv (
model		varchar2(20)	not null,
price		integer 	not null,
screen_size	integer		not null,
primary key (model)
);

create table lcdtv (
model		varchar2(20)	not null,
price		integer 	not null,
screen_size	integer		not null,
primary key (model)
);

create table pc (
model	varchar2(10)	not null,
code	varchar2(10)	not null,
type	varchar2(10) 	not null,
price	integer 	not null,
cpu	integer 	not null,
primary key (model, code)
);

create table server (
model	varchar2(10)	not null,
code	varchar2(10)	not null,
price	integer 	not null,
cpu	integer 	not null,
primary key (model, code)
);

create table tv (
model		varchar2(10)	not null,
code		varchar2(10)	not null,
type		varchar2(10) 	not null,
price		integer 	not null,
screen_size	integer 	not null,
primary key (model, code)
);

commit;

insert into desktop values ('D101', 100, 300);
insert into desktop values ('D102', 50, 100);
insert into desktop values ('D103', 400, 700);
insert into desktop values ('D104', 200, 600);
insert into desktop values ('D105', 80, 200);
insert into desktop values ('D106', 70, 210);
insert into desktop values ('D107', 200, 280);
insert into desktop values ('D108', 200, 310);
insert into desktop values ('D109', 40, 80);
insert into desktop values ('D110', 100, 320);
insert into desktop values ('D111', 90, 380);
insert into desktop values ('D112', 110, 300);

commit;

insert into laptop values ('L201', 200, 300, 800);
insert into laptop values ('L202', 120, 180, 600);
insert into laptop values ('L203', 240, 320, 1000);
insert into laptop values ('L204', 340, 400, 900);
insert into laptop values ('L205', 500, 600, 600);
insert into laptop values ('L206', 400, 400, 800);
insert into laptop values ('L207', 270, 330, 600);
insert into laptop values ('L208', 180, 200, 700);
insert into laptop values ('L209', 250, 250, 500);

commit;

insert into hdtv values ('H301', 500, 500);
insert into hdtv values ('H302', 600, 700);
insert into hdtv values ('H303', 400, 480);
insert into hdtv values ('H304', 400, 460);
insert into hdtv values ('H305', 500, 530);
insert into hdtv values ('H306', 530, 500);
insert into hdtv values ('H307', 600, 670);
insert into hdtv values ('H308', 400, 300);
insert into hdtv values ('H309', 300, 280);

commit;

insert into pdptv values ('P401', 370, 510);
insert into pdptv values ('P402', 340, 500);
insert into pdptv values ('P403', 280, 400);
insert into pdptv values ('P404', 450, 570);
insert into pdptv values ('P405', 400, 550);
insert into pdptv values ('P406', 500, 610);
insert into pdptv values ('P407', 520, 630);
insert into pdptv values ('P408', 470, 540);
insert into pdptv values ('P409', 260, 410);

commit;

insert into lcdtv values ('T501', 700, 500);
insert into lcdtv values ('T502', 760, 530);
insert into lcdtv values ('T503', 780, 540);
insert into lcdtv values ('T504', 580, 400);
insert into lcdtv values ('T505', 500, 320);
insert into lcdtv values ('T506', 650, 480);
insert into lcdtv values ('T507', 680, 490);
insert into lcdtv values ('T508', 800, 570);
insert into lcdtv values ('T509', 780, 560);
insert into lcdtv values ('T510', 630, 450);

commit;

insert into pc values ('D101', 'z', 'D', 100, 300);
insert into pc values ('P101', 'a', 'D', 110, 300);
insert into pc values ('P102', 'b', 'D', 120, 310);
insert into pc values ('P103', 'c', 'D', 150, 320);
insert into pc values ('P104', 'd', 'D', 200, 400);
insert into pc values ('P105', 'e', 'D', 240, 410);
insert into pc values ('P106', 'f', 'D', 180, 340);
insert into pc values ('P107', 'g', 'D', 80, 250);
insert into pc values ('P108', 'h', 'D', 70, 200);
insert into pc values ('P109', 'i', 'D', 300, 480);
insert into pc values ('L101', 'j', 'L', 190, 300);
insert into pc values ('L102', 'k', 'L', 200, 320);
insert into pc values ('L103', 'l', 'L', 250, 340);
insert into pc values ('L104', 'm', 'L', 300, 380);
insert into pc values ('L105', 'n', 'L', 320, 400);
insert into pc values ('L106', 'o', 'L', 170, 280);
insert into pc values ('L107', 'p', 'L', 400, 500);
insert into pc values ('L108', 'q', 'L', 360, 420);
insert into pc values ('L109', 'r', 'L', 120, 250);

commit;

insert into server values ('S101', 'a', 400, 460);
insert into server values ('S102', 'b', 500, 700);
insert into server values ('S103', 'c', 450, 520);
insert into server values ('S104', 'd', 300, 380);
insert into server values ('S105', 'e', 320, 390);
insert into server values ('S106', 'f', 370, 400);
insert into server values ('S107', 'g', 210, 280);
insert into server values ('S108', 'h', 410, 480);

commit;

insert into tv values ('H101', 'a', 'H', 500, 500);
insert into tv values ('H102', 'b', 'H', 400, 340);
insert into tv values ('H103', 'c', 'H', 510, 510);
insert into tv values ('H104', 'd', 'H', 450, 400);
insert into tv values ('H105', 'e', 'H', 470, 430);
insert into tv values ('H106', 'f', 'H', 600, 590);
insert into tv values ('H107', 'g', 'H', 300, 200);
insert into tv values ('P101', 'h', 'P', 380, 500);
insert into tv values ('P102', 'i', 'P', 310, 440);
insert into tv values ('P103', 'j', 'P', 340, 470);
insert into tv values ('P104', 'k', 'P', 290, 400);
insert into tv values ('P105', 'l', 'P', 400, 540);
insert into tv values ('P106', 'm', 'P', 600, 700);
insert into tv values ('T101', 'n', 'L', 700, 550);
insert into tv values ('T102', 'o', 'L', 740, 560);
insert into tv values ('T103', 'p', 'L', 560, 390);
insert into tv values ('T104', 'q', 'L', 610, 430);
insert into tv values ('T105', 'r', 'L', 760, 580);
insert into tv values ('T106', 's', 'L', 500, 350);
insert into tv values ('T107', 's', 'L', 510, 350);

commit;
