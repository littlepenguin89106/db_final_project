create database Team8;
use Team8;

-- entity

create table Algorithm (
    algo_id int auto_increment,
    name varchar(100),
    description text,
    primary key (algo_id)
);

create table Dataset (
    ds_id int auto_increment,
    name varchar(150),
    description text,
--  size numeric,
    attribute varchar(100),
    primary key (ds_id)
);

create table Paper (
    paper_id int auto_increment,
    name varchar(200),
    author varchar(200),
    publication varchar(50),
    published_date date,
    description text,
    primary key (paper_id)
);

create table Bulletin (
    bulletin_id int auto_increment,
    author varchar(50),
    description text,
    primary key (bulletin_id)
);

create table Task (
    task_id int auto_increment,
    name varchar(100),
    primary key (task_id)
);

/*
create table Subtask (
    subtask_id int auto_increment,
    task_id int,
    name varchar(50),
    description text,
    primary key (subtask_id),
    foreign key (task_id) references Task(task_id)
);
*/

-- relation

/*
create table applies (
    subtask_id int,
    algo_id int,
    foreign key (subtask_id) references Subtask(subtask_id),
    foreign key (algo_id) references Algorithm(algo_id),
    constraint pk_applies primary key (subtask_id,algo_id)
);

create table uses (
    algo_id int,
    ds_id int,
    foreign key (algo_id) references Algorithm(algo_id),
    foreign key (ds_id) references Dataset(ds_id),
    constraint pk_uses primary key (algo_id,ds_id)
);


create table ds_paper (
    ds_id int,
    paper_id int,
    foreign key (ds_id) references Dataset(ds_id),
    foreign key (paper_id) references Paper(paper_id),
    constraint pk_ds_paper primary key (ds_id,paper_id)
);

create table edit (
    paper_id int,
    bulletin_id int,
    foreign key (paper_id) references Paper(paper_id),
    foreign key (bulletin_id) references Bulletin(bulletin_id),
    constraint pk_edit primary key (paper_id,bulletin_id)
);
*/

create table algo_paper (
    algo_id int,
    paper_id int,
    foreign key (algo_id) references Algorithm(algo_id),
    foreign key (paper_id) references Paper(paper_id),
    constraint pk_algo_paper primary key (algo_id,paper_id)
);

create table paper_task (
    paper_id int,
    task_id int,
    foreign key (paper_id) references Paper(paper_id),
    foreign key (task_id) references Task(task_id),
    constraint pk_paper_task primary key (paper_id, task_id)
);

create table ds_task (
    task_id int,
    ds_id int,
    foreign key (task_id) references Task(task_id),
    foreign key (ds_id) references Dataset(ds_id),
    constraint pk_ds_task primary key (task_id, ds_id)
);
