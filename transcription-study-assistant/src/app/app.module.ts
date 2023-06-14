import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { Router } from '@angular/router';

import { Component, OnInit } from '@angular/core';

import {MatDialog, MAT_DIALOG_DATA} from '@angular/material/dialog';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';



import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { NewUserComponent } from './new-user/new-user.component';
import { ForgotPasswordComponent } from './forgot-password/forgot-password.component';
import { UploadLecturesComponent } from './upload-lectures/upload-lectures.component';
import { StudyMaterialsComponent } from './study-materials/study-materials.component';
import { EditorComponent } from './editor/editor.component';
import { SummariesComponent } from './summaries/summaries.component';
import { BrowsePageComponent } from './browse-page/browse-page.component';
import { AccountInformationComponent } from './account-information/account-information.component';
import { StoredInformationComponent } from './stored-information/stored-information.component';
import { NotecardsComponent } from './study-materials/notecards/notecards.component';
import { QuizzesComponent } from './study-materials/quizzes/quizzes.component';
import { SelectFilesPopUpComponent } from './select-files-pop-up/select-files-pop-up.component';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import {
  MatTabsModule,
} from '@angular/material/tabs';
import { QandaComponent } from './qanda/qanda.component';
import { SearchComponent } from './search/search.component';
//import { PopUpLecturesSelctionComponent } from './pop-up-lectures-selction/pop-up-lectures-selction.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HomeComponent,
    NewUserComponent,
    ForgotPasswordComponent,
    UploadLecturesComponent,
    EditorComponent,
    SummariesComponent,
    BrowsePageComponent,
    AccountInformationComponent,
    StoredInformationComponent,
    NotecardsComponent,
    QuizzesComponent,
    SelectFilesPopUpComponent,
    QandaComponent,
    SearchComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatTabsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { 
}

platformBrowserDynamic().bootstrapModule(AppModule);

