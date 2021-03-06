drop database if exists fang;

create database fang default charset utf8 collate utf8_bin;
	
use fang;

drop table if exists tb_agent;

drop table if exists tb_agent_estate;

drop table if exists tb_district;

drop table if exists tb_estate;

drop table if exists tb_house_info;

drop table if exists tb_house_photo;

drop table if exists tb_house_tag;

drop table if exists tb_house_type;

drop table if exists tb_login_log;

drop table if exists tb_record;

drop table if exists tb_tag;

drop table if exists tb_user;

/* Table: tb_agent */
create table tb_agent
(
   agentid              int not null auto_increment,
   name                 varchar(255) not null,
   tel                  varchar(20) not null,
   servstar             int not null default 0,
   realstar             int not null default 0,
   profstar             int not null default 0,
   certificated         bool not null default 0,
   primary key (agentid)
);

/* Table: tb_agent_estate */
create table tb_agent_estate
(
   agent_estate_id      int not null auto_increment,
	 agentid              int not null,
   estateid             int not null,
   primary key (agent_estate_id)
);


/* Index: uni_idx_agent_estate */
create unique index uni_idx_agent_estate on tb_agent_estate
(
   agentid,
   estateid
);

/* Table: tb_district */
create table tb_district
(
   distid               int not null,
   pid                  int,
   name                 varchar(255) not null,
   intro                varchar(255) default '',
   primary key (distid)
);

/* Table: tb_estate */
create table tb_estate
(
   estateid             int not null auto_increment,
   distid               int not null,
   name                 varchar(255) not null,
	 hot                  int default 0,
   intro                varchar(511) default '',
   primary key (estateid)
);

/* Table: tb_house_info */
create table tb_house_info
(
   houseid              int not null auto_increment,
   title                varchar(50) not null,
   area                 int not null,
   floor                int not null,
   totalfloor           int not null,
   direction            varchar(10) not null,
   price                int not null,
   priceunit            varchar(10) not null,
   detail               varchar(511) default '',
   mainphoto            varchar(255) not null,
   pubdate              timestamp not null default now(),
   street               varchar(255) not null,
   hassubway            bool not null default 0,
   isshared             bool not null default 0,
   hasagentfees         bool not null default 0,
   typeid               int not null,
   userid               int not null,
   distid               int not null,
   estateid             int,
   agentid              int,
   primary key (houseid)
);

/* Table: tb_house_photo */
create table tb_house_photo
(
   photoid              int not null auto_increment,
   houseid              int not null,
   path                 varchar(255) not null,
   primary key (photoid)
);

/* Table: tb_house_tag */
create table tb_house_tag
(
	 house_tag_id         int not null auto_increment,
	 houseid              int not null,
   tagid                int not null,
   primary key (house_tag_id)
);

/* Index: uni_idx_house_tag */
create unique index uni_idx_house_tag on tb_house_tag
(
   houseid,
   tagid
);

/* Table: tb_house_type */
create table tb_house_type
(
   typeid               int not null,
   name                 varchar(255) not null,
   primary key (typeid)
);

/* Table: tb_login_log */
create table tb_login_log
(
   logid                bigint not null auto_increment,
   userid               int not null,
   ipaddr               varchar(255) not null,
   logdate              timestamp not null default now(),
   devcode              varchar(255) not null default '',
   primary key (logid)
);

/* Table: tb_record */
create table tb_record
(
   recordid             bigint not null auto_increment,
   userid               int not null,
   houseid              int not null,
   recorddate           timestamp not null default now(),
   primary key (recordid)
);

/* Index: uni_idx_record */
create unique index uni_idx_record on tb_record
(
   userid,
   houseid
);

/* Table: tb_tag */
create table tb_tag
(
   tagid                int not null auto_increment,
   name                 varchar(20) not null,
   primary key (tagid)
);

/* Table: tb_user */
create table tb_user
(
   userid               int not null auto_increment,
   username             varchar(20) not null,
   password             char(32) not null,
   realname             varchar(20) not null,
   tel                  varchar(20) not null,
   email                varchar(255) not null,
	 createdate           timestamp not null default now(),
   token                char(32) not null,
   point                int not null default 0,
   isagent              bool not null default 0,
	 lastvisit            timestamp not null default now(),
   primary key (userid)
);

/* Index: uni_idx_username */
create unique index uni_idx_username on tb_user
(
   username
);

/* Index: uni_idx_tel */
create unique index uni_idx_tel on tb_user
(
   tel
);

/* Index: uni_idx_email */
create unique index uni_idx_email on tb_user
(
   email
);

alter table tb_agent_estate add constraint FK_agent_estate_agentid foreign key (agentid)
      references tb_agent (agentid) on delete restrict on update restrict;

alter table tb_agent_estate add constraint FK_agent_estate_estateid foreign key (estateid)
      references tb_estate (estateid) on delete restrict on update restrict;

alter table tb_district add constraint FK_district_pid foreign key (pid)
      references tb_district (distid) on delete restrict on update restrict;

alter table tb_estate add constraint FK_estate_distid foreign key (distid)
      references tb_district (distid) on delete restrict on update restrict;

alter table tb_house_info add constraint FK_house_info_agentid foreign key (agentid)
      references tb_agent (agentid) on delete restrict on update restrict;

alter table tb_house_info add constraint FK_house_info_distid foreign key (distid)
      references tb_district (distid) on delete restrict on update restrict;

alter table tb_house_info add constraint FK_house_info_estateid foreign key (estateid)
      references tb_estate (estateid) on delete restrict on update restrict;

alter table tb_house_info add constraint FK_house_info_typeid foreign key (typeid)
      references tb_house_type (typeid) on delete restrict on update restrict;

alter table tb_house_info add constraint FK_house_info_userid foreign key (userid)
      references tb_user (userid) on delete restrict on update restrict;

alter table tb_house_photo add constraint FK_house_photo_houseid foreign key (houseid)
      references tb_house_info (houseid) on delete restrict on update restrict;

alter table tb_house_tag add constraint FK_house_tag_houseid foreign key (houseid)
      references tb_house_info (houseid) on delete restrict on update restrict;

alter table tb_house_tag add constraint FK_house_tag_tagid foreign key (tagid)
      references tb_tag (tagid) on delete restrict on update restrict;

alter table tb_login_log add constraint FK_login_log_userid foreign key (userid)
      references tb_user (userid) on delete restrict on update restrict;

alter table tb_record add constraint FK_record_houseid foreign key (houseid)
      references tb_house_info (houseid) on delete restrict on update restrict;

alter table tb_record add constraint FK_record_userid foreign key (userid)
      references tb_user (userid) on delete restrict on update restrict;