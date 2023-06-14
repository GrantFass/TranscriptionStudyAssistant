import { Component } from '@angular/core';
import { NewUser } from '../newuser';
import { CommunicationsService } from '../communications.service';
import { USERS } from 'mock-users';
import { HttpClientModule } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-new-user',
  templateUrl: './new-user.component.html',
  styleUrls: ['./new-user.component.css']
})
export class NewUserComponent {

  new: NewUser[] = [];

  constructor(private communicationsService: CommunicationsService, private http: HttpClient){

  }

  sendData(): void {
    const body = {
      "ts": 1666818622000,
      "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
      "p": {
        "email": "example@mail.net",
        "password": "QwertY123!",
        "birthday": "12/25/1970",
        "org": "MSOE",
        "first": "Jane",
        "last": "Doe",
        "gender": 3,
        "phone": 12345678901,
        "job": 0,
        "username": "DoeJ1970"
      }
    }
    
    const headers = { 'Content-Type': 'application/json' };
    const users = this.http.post('/fb/auth/new', body, {headers}).subscribe((response) => {
      console.log(response);
    }, (error) => {
      console.error(error)
    });
    // this.communicationsService.add('Adding a New User');
    // return users;
  }

  // ngOnInit(): void {
  //   const body = {
  //     "ts": 1666818622000,
  //     "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  //     "p": {
  //       "email": "example@mail.net",
  //       "password": "QwertY123!",
  //       "birthday": "12/25/1970",
  //       "org": "MSOE",
  //       "first": "Jane",
  //       "last": "Doe",
  //       "gender": 3,
  //       "phone": 12345678901,
  //       "job": 0,
  //       "username": "DoeJ1970"
  //     }
  //   }
  //   const headers = { 'Content-Type': 'application/json' };
    
  //   const users = this.http.get('http://localhost:8844/fb/auth/new').subscribe((response) => {
  //     console.log(response);
  //   }, (error) => {
  //     console.error(error)
  //   });
  //   // this.communicationsService.add('Adding a New User');
  //   // return users;
  // }
}
