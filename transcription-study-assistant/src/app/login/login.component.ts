import { Component, OnInit } from '@angular/core';
import { NewUser } from '../newuser';
import { CommunicationsService } from '../communications.service';
import { USERS } from 'mock-users';
import { HttpClientModule } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { FileUploadService } from 'src/app/services/file-upload.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent {

  constructor(private communicationsService: CommunicationsService, private http: HttpClient, private uploadService: FileUploadService) {

  }

  sendData(): void {
    const body = {
      "ts": 1666818622000,
      "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
      "p": {
        "username": "DoeJ1970",
        "password": "QwertY123!",
        "ip": "75.103.1.21",
        "os": "Microsoft Windows (build 103)",
        "browser": "Mozilla Firefox (build 1.1.2)",
        "device": "Unknown",
        "location": "Milwaukee WI",
        "redirect": "example.com/index"
      }
    }
  


    const headers = { 'Content-Type': 'application/json' };
    const users = this.http.post('/fb/auth/in', body, { headers }).subscribe((response) => {
      console.log(response);
      console.log(body);
    }, (error) => {
      console.error(error)
    });
    //this.communicationsService.add('Adding a New User');
    //return users;
  }
}
