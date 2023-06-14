import { Injectable } from '@angular/core';
import { NewUser } from './newuser';
import { USERS } from 'mock-users';

//import DATA TYPES LIKE HERO


@Injectable({
  //provider creates and initial instance of this service
  providedIn: 'root'
})
export class CommunicationsService {

  constructor() { }

  getNewUsers(): NewUser[]{
    return USERS;
  }
}
