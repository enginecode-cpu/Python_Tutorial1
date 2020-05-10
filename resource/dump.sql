BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRMARY KEY, username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'Kim','Kim@google.com','000-1234-5678','Kim.com','2019-07-09 19:03:55');
INSERT INTO "users" VALUES(2,'Park','Park@naver.com','010-5678-1234','Park.com','2019-07-09 19:03:55');
INSERT INTO "users" VALUES(3,'Lee','Lee@daum.net','010-3333-3333','Lee.com','2019-07-09 19:03:55');
INSERT INTO "users" VALUES(4,'Cho','Cho@google.com','010-5555-5555','Cho.com','2019-07-09 19:03:55');
INSERT INTO "users" VALUES(5,'You','You@naver.com','010-7777-7777','You.com','2019-07-09 19:03:55');
COMMIT;
