import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { NewUserComponent } from './new-user/new-user.component';
import { ForgotPasswordComponent } from './forgot-password/forgot-password.component';
import { SummariesComponent } from './summaries/summaries.component';
import { StudyMaterialsComponent } from './study-materials/study-materials.component';
import { UploadLecturesComponent } from './upload-lectures/upload-lectures.component';
import { EditorComponent } from './editor/editor.component';
import { AccountInformationComponent } from './account-information/account-information.component';
import { StoredInformationComponent } from './stored-information/stored-information.component';
import { NotecardsComponent } from './study-materials/notecards/notecards.component';
import { QuizzesComponent } from './study-materials/quizzes/quizzes.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: '', redirectTo: 'home', pathMatch:'full'},
  { path: 'list/:user/:userID', component: AppComponent },
  {path: 'login', component: LoginComponent},
  {path: 'new-user', component: NewUserComponent},
  {path: 'forgot-password', component: ForgotPasswordComponent},
  {path: 'summaries', component: SummariesComponent},
  {path: 'study-materials', component: StudyMaterialsComponent},
  {path: 'upload-lectures', component: UploadLecturesComponent},
  {path: 'editor', component: EditorComponent},
  {path: 'account-information', component: AccountInformationComponent},
  {path: 'stored-information', component: StoredInformationComponent},
  {path: 'study-materials/notecards', component: NotecardsComponent},
  {path: 'study-materials/quizzes', component: QuizzesComponent},
  {path: '**', redirectTo: 'home'}
];

@NgModule({
  declarations: [],
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
